import uuid


def generate_chunks(message, packet_size):
    chunks = []
    i = 0
    while i < len(message) and i+packet_size <= len(message):
        chunks.append(message[i:i+packet_size])
        i += packet_size
    if i != len(message):
        chunks.append(message[i-packet_size:])
    return chunks

def generate_packets(chunks, source_ip, destination_ip):
    packets = []
    for chunk in chunks:
        packet_id = uuid.uuid4()
        source_ip = source_ip
        destination_ip = destination_ip
        message = chunk
        packets.append({"packet_id":packet_id, "source_ip":source_ip, "destination_ip":destination_ip,"message":message})
    return packets
#sample implementation

message = "hi i am trying to understand basic tcp structure"
source_ip = "130.303.20.1"
destination_ip = "19.134.243.98"
packet_size = 10 #<= 10 characters per packet

chunks = generate_chunks(message, packet_size)

packets = generate_packets(chunks, source_ip, destination_ip)

print(packets)