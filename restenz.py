def ecor1(seq, enzima):
    sitiocorte = seq.find(enzima)
    frag1 = seq[:sitiocorte + len(enzima)]
    frag2 = seq[sitiocorte + len(enzima):]

    # Complementar los fragmentos
    frag1_complemento = frag1[::-1]
    frag2_complemento = frag2[::-1]

    return [
        [frag1, len(frag1)],
        [frag1_complemento, len(frag1_complemento)],
        [frag2, len(frag2)],
        [frag2_complemento, len(frag2_complemento)]
    ]