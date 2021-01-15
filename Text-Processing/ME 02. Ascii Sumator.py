start_ch = ord(input())
end_ch = ord(input())

text =input()
sum =0
for ch in text:
    if start_ch<ord(ch)<end_ch:
        sum+=ord(ch)

print(sum)