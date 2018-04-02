from flask import Flask
app = Flask(__name__)

@app.route("/<int:n>")
def prime(n):
    def find_primes(n):
        result = []
        for p in range(2, n+1):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                result.append(p)
        return result

    return str(find_primes(n))
