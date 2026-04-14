import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.array(T)
    
    pts = np.array(points)
    is_single = pts.ndim == 1

    if is_single:
        pts = pts.reshape(1, 3)

    N = pts.shape[0]

    ones = np.ones((N, 1), dtype=pts.dtype)
    pts_h = np.hstack((pts, ones))

    transformed_h = pts_h @ T.T

    transformed = transformed_h[:, :3]

    return transformed[0] if is_single else transformed