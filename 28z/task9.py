def TheRabbitsFoot(raw_s: str, encode: bool) -> str:
    # Decryption algorithm
    if not encode:
        words: list[str] = raw_s.split()
        words_len: int = len(raw_s.replace(" ", ""))
        words_count: int = len(words)
        s_decrypted: str = ""
        for i in range(words_len):
            s_decrypted += words[i % words_count][i // words_count]
        return s_decrypted

    # Encryption algorithm
    # Remove spaces from a string
    s: str = raw_s.replace(" ", "")
    # Determine the matrix dimensions
    s_len: int = len(s)
    m_dim: int = 0
    n_dim: int = 0
    for i in range(1, s_len + 1):
        if i * i >= s_len:
            m_dim = i - 1
            n_dim = i
            break
    if m_dim * n_dim < s_len:
        m_dim += 1
    # Create a matrix of characters
    matrix: list[list[str]] = []
    for i in range(m_dim):
        row: list[str] = []
        for j in range(n_dim):
            if i * n_dim + j < s_len:
                row.append(s[i * n_dim + j])
            else:
                row.append("")
        matrix.append(row)
    # Create an encrypted message
    s_encrypted: str = ""
    for i in range(m_dim * n_dim):
        s_encrypted += matrix[i % m_dim][i // m_dim]
        if i % m_dim == m_dim - 1 and i // m_dim != n_dim - 1:
            s_encrypted += " "
    return s_encrypted



