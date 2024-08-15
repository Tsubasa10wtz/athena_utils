### 说明
每个目录下，例如inf/resnet_imagenet_cache,inf代表所用的实例类型，
resnet和imagenet代表所用的模型和数据集，cache代表的是否提前缓存
每张图的横轴是时间，纵轴代表一个io
all是整体，first576是前576个（为什么取576和batch、num_workers设置有关）
second代表first之后的64个（这里是一个batch）