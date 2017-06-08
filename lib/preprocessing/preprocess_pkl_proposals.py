
"""

Loading the pickle proposals generated by py-faster-rcnn and generates hdf5 files ready to train the network.

"""



def generate_hdf5(dataset):
    return 0

def get_feature_boxes(im, boxes, net):
    for bbox in boxes[:3]:
        x, y = (bbox[0], bbox[1])
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        y_2 = y + height
        x_2 = x + width

        image = im[int(round(y)):int(round(y_2)), int(round(x)):int(round(x_2))]
        image = resize(image, (224, 224))
        image = np.rollaxis(image, 2, 1)
        image = np.rollaxis(image, 1, 0)
        image = image[np.newaxis, :, :, :]
    

features = imagenet_test(im,imdb_boxes[i], net=net_box_to_feat)


if __name__ == '__main__':
    