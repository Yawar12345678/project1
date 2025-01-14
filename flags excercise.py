def printb(value):
    print(f"{value:08b}")
class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4
    NORMALIZE = O = 8
    REMOVECLICKS = R = 16
def process_audio(flags):
    lookup = {
        Flags.LOUDER: "Making Louder",
        Flags.DENOISE: "Removing Noise",
        Flags.DEESS: "De-essing",
        Flags.NORMALIZE: "Normalizing",
        Flags.REMOVECLICKS: "Removing clicks",
     }
    for flag, description in lookup.items():
       if flag & flags:
          print(f"{description}...")
        
    
    def main():
        combined_flags1 = Flags.L | Flags.N
        process_audio(combined_flags1)
    if __name__ ==  "__main__":
            main()





