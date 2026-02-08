import hashlib

def hash_name(name):
    return hashlib.sha256(name.lower().strip().encode()).hexdigest()


def love_calculator(name1, name2):
    # 🔒 Hash inputs
    h1 = hash_name(name1)
    h2 = hash_name(name2)

    # 💯 Hidden destiny hashes (Shishir + Supriya)
    SPECIAL_HASHES = {
        "e12a728fd8bda773f60908e573ff8d5856567a397dc48a2314ea8cf4b5e8d28a",  # shishir
        "25e5962f4841dcba67697f669d3c7ca4bc9aceafdda73a408a465dbb833f14df"   # supriya
    }

    # 💖 Absolute rule (no math, just fate)
    if {h1, h2} == SPECIAL_HASHES:
        return 100

    # 🔢 Normal calculation logic
    n1 = name1.lower().replace(" ", "")
    n2 = name2.lower().replace(" ", "")

    # 1️⃣ Length score
    len_score = (min(len(n1), len(n2)) / max(len(n1), len(n2))) * 30

    # 2️⃣ Common alphabet score
    common_chars = set(n1) & set(n2)
    alpha_score = (len(common_chars) / 26) * 30

    # 3️⃣ Longest common substring score
    def lcs(a, b):
        longest = 0
        for i in range(len(a)):
            for j in range(len(b)):
                k = 0
                while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                    k += 1
                longest = max(longest, k)
        return longest

    lcs_score = (lcs(n1, n2) / max(len(n1), len(n2))) * 40

    # ❤️ Final love percentage (max 99 for normal cases)
    return min(int(len_score + alpha_score + lcs_score), 99)


# 🧪 Example usage
if __name__ == "__main__":
    a = input("Enter first name: ")
    b = input("Enter second name: ")
    print(f"❤️ Love Percentage: {love_calculator(a, b)}%")
