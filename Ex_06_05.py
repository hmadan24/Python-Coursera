text = "X-DSPAM-Confidence:    0.8475";
start_pos = text.find('0')
print(float(text[start_pos:]))