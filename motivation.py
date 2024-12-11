import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 定义辅助函数
def make_patch_spines_invisible(ax):
    """设置不可见的轴"""
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def alignYaxes(axes, align_values=None):
    """多 y 轴对齐函数"""
    from matplotlib.pyplot import MaxNLocator
    nax = len(axes)
    ticks = [aii.get_yticks() for aii in axes]
    if align_values is None:
        aligns = [ticks[ii][0] for ii in range(nax)]
    else:
        if len(align_values) != nax:
            raise Exception("Length of <axes> doesn't equal that of <align_values>.")
        aligns = align_values

    bounds = [aii.get_ylim() for aii in axes]

    ticks_align = [ticks[ii] - aligns[ii] for ii in range(nax)]
    ranges = [tii[-1] - tii[0] for tii in ticks]
    lgs = [-np.log10(rii) + 2. for rii in ranges]
    igs = [np.floor(ii) for ii in lgs]
    log_ticks = [ticks_align[ii] * (10.**igs[ii]) for ii in range(nax)]

    comb_ticks = np.concatenate(log_ticks)
    comb_ticks.sort()
    locator = MaxNLocator(nbins='auto', steps=[1, 2, 2.5, 3, 4, 5, 8, 10])
    new_ticks = locator.tick_values(comb_ticks[0], comb_ticks[-1])
    new_ticks = [new_ticks / 10.**igs[ii] for ii in range(nax)]
    new_ticks = [new_ticks[ii] + aligns[ii] for ii in range(nax)]

    idx_l = 0
    for i in range(len(new_ticks[0])):
        if any([new_ticks[jj][i] > bounds[jj][0] for jj in range(nax)]):
            idx_l = i - 1
            break

    idx_r = 0
    for i in range(len(new_ticks[0])):
        if all([new_ticks[jj][i] > bounds[jj][1] for jj in range(nax)]):
            idx_r = i
            break

    new_ticks = [tii[idx_l:idx_r+1] for tii in new_ticks]
    for axii, tii in zip(axes, new_ticks):
        axii.set_yticks(tii)

    return new_ticks

# 定义绘图函数
def plotLines(x, y1, y2, ax):
    ax.plot(x, y1, 'b-', label='CDF')
    ax.tick_params('y', colors='b')
    ax.set_ylabel('CDF', color='b')

    tax1 = ax.twinx()
    tax1.hist(y2, bins=100, color='orange', alpha=0.6, label='Frequency Distribution')
    tax1.tick_params('y', colors='orange')
    tax1.set_ylabel('Count', color='orange')

    return ax, tax1

# 生成数据
ids = np.random.randint(0, 50000, size=500000)
diff_list = [abs(ids[i] - ids[i - 1]) for i in range(1, len(ids))]
cdf = np.arange(1, len(diff_list) + 1) / len(diff_list)

# 绘制图表
figure, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=100)

# 不对齐的图
ax1, tax1_1 = plotLines(diff_list[:500], cdf[:500], diff_list, axes[0])
axes[0].set_title('No alignment')

# 对齐的图
ax2, tax2_1 = plotLines(diff_list[:500], cdf[:500], diff_list, axes[1])
alignYaxes([ax2, tax2_1])
axes[1].set_title('Aligned')

figure.tight_layout()
plt.show()