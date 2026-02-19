# HTTP request compression

- Compress http body with Gzip
- Content-Encoding: gzip

- Apache supports Input Decompression in mod\_deflate: <http://httpd.apache.org/docs/2.2/mod/mod_deflate.html#enable>
  - <https://blog.art-of-coding.eu/compressed-http-requests/> mentions some bugs.

- NginX: [thread1](https://www.ruby-forum.com/topic/4422268) and [thread2](http://forum.nginx.org/read.php?11,96472,214266) indicate that this is not supported by NginX.

#### Read more

- [HTTP response compression and related security exploits](/web/20210226164451/https://wiki.cantara.no/display/dev/HTTP+response+compression+and+related+security+exploits "HTTP response compression and related security exploits")

- <http://stackoverflow.com/questions/7153484/gzip-post-request-with-httpclient-in-java>

- <http://serverfault.com/questions/56700/is-it-possible-to-enable-http-compression-for-requests>

- <http://www.agent31.eu/2007/07/compressed-http.html>

- <https://blog.art-of-coding.eu/compressed-http-requests/>
