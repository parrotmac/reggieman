import collections
import os
import uuid

import redis
from flask import Flask
from flask import request, redirect, render_template

app = Flask(__name__)

r = redis.StrictRedis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=os.environ.get("REDIS_PORT", "6379"),
    password=os.environ.get("REDIS_PASSWORD")
)

# This was going to be a really crappy auth system.
# But it's crappy, so let's just wait and do something better
# management_secret = os.environ.get("MANAGER_SECRET")
#
# if management_secret is None:
#     management_secret = uuid.uuid4()
#     # Warning: prints temporary key to STDOUT
#     print("Management Secret: %s" % management_secret)


service_url = os.environ.get("SERVICE_SUFFIX", "/")

@app.route('/', methods=['GET', "POST"])
def hello_world():
    messages = []
    if request.method == "POST":

        if 'delete' in request.form.keys():
            delete_this_key = request.form.get("delete")
            r.delete(delete_this_key)
            messages.append({'type': 'success', 'text': "Deleted key '%s'" % delete_this_key})
        else:
            update_redis_key = request.form.get("redisKey")
            update_redis_value = request.form.get("redisValue")
            if update_redis_key.strip() != "":

                r.set(update_redis_key, update_redis_value)

                messages.append({'type': 'success', "text": "Value updated"})
                return redirect(service_url, code=302)
            else:
                messages.append({'type': 'error', 'text': "Error: Redis key is invalid"})

    redis_strings = {}
    for redis_key in r.keys("*"):
        if r.type(redis_key.decode('utf-8')).decode("utf-8") == "string":
            redis_strings[redis_key.decode('utf-8')] = r.get(redis_key.decode('utf-8')).decode("utf-8")

    current_redis_key = request.args.get("key")

    sorted_redis_strings = collections.OrderedDict(sorted(redis_strings.items()))

    template_data = {
        "redis_strings": sorted_redis_strings,
        "service_url": service_url
    }

    if current_redis_key is not None:
        template_data["current_redis_key"] = current_redis_key
        template_data["current_redis_value"] = r.get(current_redis_key).decode('utf-8')

    return render_template("editor.html", data=template_data)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
