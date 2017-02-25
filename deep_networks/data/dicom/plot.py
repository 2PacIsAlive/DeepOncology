import logging
#import pylab
import matplotlib.pyplot as plt
from skimage import measure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Plotter(object):

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def plot_3d(self, image, threshold=-300):
        """
    
        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
        """
        # Position the scan upright, 
        # so the head of the patient would be at the top facing the camera
        p = image.transpose(2,1,0)
        verts, faces = measure.marching_cubes(p, threshold)
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        # Fancy indexing: `verts[faces]` to generate a collection of triangles
        mesh = Poly3DCollection(verts[faces], alpha=0.1)
        face_color = [0.5, 0.5, 1]
        mesh.set_facecolor(face_color)
        ax.add_collection3d(mesh)
        ax.set_xlim(0, p.shape[0])
        ax.set_ylim(0, p.shape[1])
        ax.set_zlim(0, p.shape[2])
        plt.show()


def plot(dataset):
    log.info("plotting {}".format(dataset.PatientsName))
    #pylab.imshow(dataset.pixel_array, cmap=pylab.cm.bone)
    
def save(dataset):
    log.info("saving {}".format(dataset.PatientsName))
    pylab.imshow(dataset.pixel_array, cmap=pylab.cm.bone)
    pylab.savefig(dataset.PatientsName + '.png', 
                    bbox_inches='tight')


