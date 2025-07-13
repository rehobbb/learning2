import math

def calculate_beta_z():
    # 欢迎信息
    print("欢迎使用《建筑结构荷载规范》GB5009-2012 风振系数βz计算器")
    print("=" * 50)
    
    # 输入基本参数
    z = float(input("请输入计算高度z（m）："))
    B = float(input("请输入结构迎风面宽度B（m）："))
    H = float(input("请输入结构总高度H（m）："))
    w0 = float(input("请输入基本风压w0（kN/m²）："))
    mu_s = float(input("请输入结构表面的风荷载体型系数μs："))
    
    # 地貌类别
    print("\n请选择地面粗糙度类别：")
    print("A类：近海海面和海岛、海岸、湖岸及沙漠地区")
    print("B类：田野、乡村、丛林、丘陵以及房屋比较稀疏的乡镇和城市郊区")
    print("C类：有密集建筑群的城市市区")
    print("D类：有密集建筑群且房屋较高的城市市区")
    terrain_type = input("请输入类别（A/B/C/D）：").upper()
    
    # 结构自振频率
    f1 = float(input("\n请输入结构基本自振频率f1（Hz）："))
    
    # 阻尼比
    xi = float(input("请输入结构阻尼比ξ（一般建筑取0.05，钢结构取0.02，有填充墙的钢结构取0.03）："))
    
    # 计算过程记录
    calculation_steps = []
    calculation_steps.append(f"计算高度z = {z} m")
    calculation_steps.append(f"结构迎风面宽度B = {B} m")
    calculation_steps.append(f"结构总高度H = {H} m")
    calculation_steps.append(f"基本风压w0 = {w0} kN/m²")
    calculation_steps.append(f"风荷载体型系数μs = {mu_s}")
    calculation_steps.append(f"地面粗糙度类别 = {terrain_type}类")
    calculation_steps.append(f"结构基本自振频率f1 = {f1} Hz")
    calculation_steps.append(f"结构阻尼比ξ = {xi}")
    calculation_steps.append("")
    
    # 1. 计算风压高度变化系数μz
    calculation_steps.append("1. 计算风压高度变化系数μz：")
    if terrain_type == 'A':
        mu_z = 1.379 * (z / 10) ** 0.24
        calculation_steps.append("  根据规范表8.2.1，A类地貌风压高度变化系数计算公式：")
        calculation_steps.append(f"  μz = 1.379 × (z/10)^0.24 = 1.379 × ({z}/10)^0.24 = {mu_z:.4f}")
    elif terrain_type == 'B':
        mu_z = 1.000 * (z / 10) ** 0.32
        calculation_steps.append("  根据规范表8.2.1，B类地貌风压高度变化系数计算公式：")
        calculation_steps.append(f"  μz = 1.000 × (z/10)^0.32 = 1.000 × ({z}/10)^0.32 = {mu_z:.4f}")
    elif terrain_type == 'C':
        mu_z = 0.616 * (z / 10) ** 0.44
        calculation_steps.append("  根据规范表8.2.1，C类地貌风压高度变化系数计算公式：")
        calculation_steps.append(f"  μz = 0.616 × (z/10)^0.44 = 0.616 × ({z}/10)^0.44 = {mu_z:.4f}")
    elif terrain_type == 'D':
        mu_z = 0.318 * (z / 10) ** 0.60
        calculation_steps.append("  根据规范表8.2.1，D类地貌风压高度变化系数计算公式：")
        calculation_steps.append(f"  μz = 0.318 × (z/10)^0.60 = 0.318 × ({z}/10)^0.60 = {mu_z:.4f}")
    else:
        print("错误：地面粗糙度类别输入错误！")
        return
    calculation_steps.append("")
    
    # 2. 计算结构刚度特征值v
    calculation_steps.append("2. 计算结构刚度特征值v：")
    v = 0.16 * (f1 * H) / (math.sqrt(w0))
    calculation_steps.append(f"  v = 0.16 × (f1×H)/√w0 = 0.16 × ({f1}×{H})/√{w0} = {v:.4f}")
    calculation_steps.append("")
    
    # 3. 计算脉动增大系数ξ
    calculation_steps.append("3. 计算脉动增大系数ξ：")
    if v <= 0.1:
        xi_factor = 1.0
    elif v >= 10:
        xi_factor = 2.0
    else:
        xi_factor = 1.0 + 0.65 * math.log10(v)
    calculation_steps.append(f"  根据规范表8.4.3，当v = {v:.4f}时，脉动增大系数插值计算：")
    calculation_steps.append(f"  ξ = 1.0 + 0.65×log10(v) = 1.0 + 0.65×log10({v}) = {xi_factor:.4f}")
    
    # 考虑阻尼比修正
    if xi != 0.05:
        xi_correction = math.sqrt(0.05 / xi)
        xi_factor = xi_factor * xi_correction
        calculation_steps.append(f"  考虑阻尼比ξ = {xi}的修正：ξ = ξ × √(0.05/ξ) = {xi_factor:.4f}")
    calculation_steps.append("")
    
    # 4. 计算脉动影响系数υ
    calculation_steps.append("4. 计算脉动影响系数υ：")
    # 计算结构顶部的风速V
    V = 29.1 * math.sqrt(w0) * mu_z
    calculation_steps.append(f"  计算结构顶部的风速V = 29.1×√w0×μz = 29.1×√{w0}×{mu_z} = {V:.2f} m/s")
    
    # 计算湍流强度I10
    if terrain_type == 'A':
        I10 = 0.12
    elif terrain_type == 'B':
        I10 = 0.16
    elif terrain_type == 'C':
        I10 = 0.22
    elif terrain_type == 'D':
        I10 = 0.30
    calculation_steps.append(f"  根据规范表8.4.4-1，{terrain_type}类地貌的湍流强度I10 = {I10}")
    
    # 计算脉动影响系数
    if H/B <= 5:
        alpha = 0.25
    else:
        alpha = 0.25 + 0.01 * (H/B - 5)
    calculation_steps.append(f"  结构高宽比H/B = {H/B:.2f}，取α = {alpha}")
    
    z_ratio = z / H
    if z_ratio <= 0.1:
        z_factor = 0.7
    elif z_ratio >= 1.0:
        z_factor = 1.0
    else:
        z_factor = 0.7 + 0.3 * (z_ratio - 0.1) / 0.9
    calculation_steps.append(f"  高度比z/H = {z_ratio:.2f}，高度修正系数z_factor = {z_factor:.2f}")
    
    upsilon = 2.2 * I10 * xi_factor * alpha * z_factor
    calculation_steps.append(f"  υ = 2.2×I10×ξ×α×z_factor = 2.2×{I10}×{xi_factor}×{alpha}×{z_factor} = {upsilon:.4f}")
    calculation_steps.append("")
    
    # 5. 计算风振系数βz
    calculation_steps.append("5. 计算风振系数βz：")
    beta_z = 1 + upsilon
    calculation_steps.append(f"  βz = 1 + υ = 1 + {upsilon:.4f} = {beta_z:.4f}")
    
    # 输出结果
    print("\n计算结果：")
    print(f"风振系数βz = {beta_z:.4f}")
    
    # 输出计算过程
    print("\n计算过程：")
    print("\n".join(calculation_steps))

if __name__ == "__main__":
    calculate_beta_z()    