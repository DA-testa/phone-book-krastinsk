# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class ContactBook:
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]
        self._prime = 1000000007
        self._multiplier = 263

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, contact):
        hashed = self._hash_func(str(contact.number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == contact.number:
                bucket[i].name = contact.name
                return
        bucket.append(contact)

    def delete(self, number):
        hashed = self._hash_func(str(number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == number:
                bucket.pop(i)
                return

    def find(self, number):
        hashed = self._hash_func(str(number))
        bucket = self.buckets[hashed]
        for contact in bucket:
            if contact.number == number:
                return contact.name
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def process_queries(queries):
    result = []
    contact_book = ContactBook()
    for query in queries:
        if query.type == 'add':
            contact_book.add(query)
        elif query.type == 'del':
            contact_book.delete(query.number)
        else:
            result.append(contact_book.find(query.number))
    return result

def write_responses(result):
    print('\n'.join(result))

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

