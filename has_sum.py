

def hasPathWithGivenSum(t, s, tot=0):
    if not t:
        return tot == s
    if t.left:
        hasPathWithGivenSum(t.left, s, tot+s)
    tot += t.value
    if t.right:
        hasPathWithGivenSum(t.right, s, tot+s)
    return tot == s


if __name__ == "__main__":
    t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        },
        "right": None
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": -3,
                "left": None,
                "right": None
            }
        }
    }
}

s = 7
# the output should be hasPathWithGivenSum(t, s) = true.
print (hasPathWithGivenSum(t, s))