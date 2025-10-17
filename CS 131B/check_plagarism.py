def check_plagiarism(file1, file2):
    with open(file1, "r") as f1:
        file1Content = f1.read().split()
    with open(file2, "r") as f2:
        file2Content = f2.read().split()

    longest_match = []
    for i in range(len(file1Content)):
        for j in range(len(file2Content)):
            if file1Content[i] == file2Content[j]:
                key1 = i
                key2 = j
                current_match = []
                while key1 < len(file1Content) and key2 < len(file2Content) and file1Content[key1] == file2Content[key2]:
                    current_match.append(file1Content[key1])
                    key1 += 1
                    key2 += 1
                if len(current_match) > len(longest_match):
                    longest_match = current_match
    if len(longest_match) > 4:
        return " ".join(longest_match)
    else:
        return False