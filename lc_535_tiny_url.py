class Codec:
    def __init__(self) -> None:
        self.url_dict = {}
        self.url_num = 0
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url_id = self.url_num
        self.url_dict[longUrl] = url_id
        self.url_num += 1
        return 'http://tinyurl.com/' + str(url_id)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url_id = int(shortUrl[19:])
        for key, value in self.url_dict.items():
            url = ''
            if value == url_id:
                url = key
                break

        return url

if __name__ == '__main__':
    c = Codec()
    print(c.encode('https://leetcode.com/problems/design-tinyurl'))
    print(c.decode('http://tinyurl.com/4'))
