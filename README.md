# Got 403? Try to bypass it with XFF headers

`docker run --rm --name forbid-bypasser -e VULN_ID=1 -e DOMAIN=site.com whitespots/forbid-bypasser`
