from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

# Hashing functions mapping
HASH_FUNCTIONS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "sha3_512": hashlib.sha3_512,
    "sha3_256": hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_224": hashlib.sha3_224,
    "sha224": hashlib.sha224,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s,
}

@app.route("/", methods=["GET", "POST"])
def index():
    hash_result = ""
    
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        algorithm = request.form.get("algorithm", "md5")

        if algorithm in HASH_FUNCTIONS:
            hash_result = HASH_FUNCTIONS[algorithm](text.encode()).hexdigest()
        elif algorithm == "shake_128":
            hash_result = hashlib.shake_128(text.encode()).hexdigest(32)
        elif algorithm == "shake_256":
            hash_result = hashlib.shake_256(text.encode()).hexdigest(32)
        else:
            hash_result = "Invalid algorithm"

    return render_template("index.html", hash_result=hash_result)

if __name__ == "__main__":
    app.run(debug=True)
