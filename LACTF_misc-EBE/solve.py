import pyshark

cap_all = pyshark.FileCapture("./EBE.pcap")
total = 0
evil = 0
normal = 0
flag = b""

for packet in cap_all:
    total += 1
    try:
        rb = packet.ip.flags_rb  # trả về 'True' hoặc 'False' dạng string
        if rb == 'True':
            evil += 1
        else:
            normal += 1
            raw_hex = packet.data.data.replace(":", "")
            word = bytes.fromhex(raw_hex)
            flag += word
    except AttributeError:
        pass

cap_all.close()

print(f"Tổng: {total}, Evil bit=1: {evil}, Evil bit=0: {normal}")
print("Flag nhận được:", flag.decode(errors='ignore'))
