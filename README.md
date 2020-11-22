# A small contribution to community :)
This is a part of our toolset for [vulneravility monitoring service](https://whitespots.io/vulnerability-monitoring)

### Check other [opensource tools](https://github.com/whitespots/fast-security-scanners)

# Got 403? Try to bypass it with XFF headers

`docker run --rm --name forbid-bypasser -e VULN_ID=1 -e PORTS=443,8080 -e DOMAIN=site.com whitespots/forbid-bypasser`
