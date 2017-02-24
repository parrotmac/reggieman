# Reggieman #

### A barebones tool for exploring, adding, or deleting Redis data ###
Originally written and Django, this Flask app is just the bare minimum required to edit redis keys. Right now it only supports editing string types.

### How do I get set up? ###

Configure your environmental variables. The defaults are listed below.
```
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=<empty>
SERVICE_URL=/
```
`SERVICE_URL` is intended to be configurable, in case your instance is running behind some sort of proxy that doesn't allow redirecting back to `/`.

## IMPORTANT: There's no authentication. ##
Please secure this behind, at the very least, HTTP Basic auth if you'll be exposing this to the public internet.

### Contribution guidelines ###

* Test your code
* Don't break this thing

### What if it is broken, or needs enhancements? ###

* Open an issue
* Fix it, or wait for someone else to fix it
* Reasonable PRs will be merged :)