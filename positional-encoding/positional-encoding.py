import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    v=[]

    for i in range(seq_len):
        inside= []
        for j in range(d_model):
            if j %2==1:
                val= np.cos(i/(base**((j-1)/d_model)))
                inside.append(val)
            else:
                val=np.sin(i/base**(j/d_model))
                inside.append(val)

        v.append(inside)

    return np.asarray(v)
            
                            
    pass