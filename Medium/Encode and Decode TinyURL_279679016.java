public class Codec {
    
   HashMap<String, String> storage = new HashMap<String, String>();
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String shortUrl = "http://tinyurl.com/";
        shortUrl+=longUrl.hashCode();
        storage.put("http://tinyurl.com/" + longUrl.hashCode(), longUrl);
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return storage.get(shortUrl);
    }
    

}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
