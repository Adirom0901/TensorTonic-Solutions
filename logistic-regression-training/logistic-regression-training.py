import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    x=X
    m,n =np.shape(x)
    w= np.zeros(n)
    b=0.0
    def forward(x,w,b):
        z = np.matmul(x,w) +b

        p= _sigmoid(z)
        return p

    def backward(p,y,x):
        dw= np.matmul(x.T,(p-y))/len(y)  
        db= np.mean(p-y)

        

        return (dw,db)

    for _ in range(steps):

        p= forward(x,w,b)

        dw,db= backward(p,y,x)

        w=w-lr*dw
        b=b-lr*db

    return (w,b)
        
        
        
    pass