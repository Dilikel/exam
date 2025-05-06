ips = [192, 168, 112, 140]
masks = [255, 255, 255, 224]

ips_bin = []
masks_bin = []
host_bin = ''

for ip in ips:
  ips_bin.append(bin(ip)[2:].zfill(8))

for mask in masks:
  masks_bin.append(bin(mask)[2:].zfill(8))

for ip_part, mask_part in zip(ips_bin, masks_bin):
  for ip_bit, mask_bit in zip(ip_part, mask_part):
    if mask_bit == '0':
      host_bin += ip_bit

print(int(host_bin, 2))