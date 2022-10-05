import pyromat as pm
pm.config["unit_pressure"] = "kPa"
pm.config["def_p"] = 100

mp_R134a = pm.get('mp.C2H2F4')

m_dot = 0.03 #kg/s <-- given
T1 = -20 + 273.15 # K <--given
T3 = 40 +273.15 # K <--given


h1 = mp_R134a.hs(T=T1)[1]
print(f"Enthalpy of refrigerant after evaporator: {round(float(h1),3)} kJ/kg")

s1 = mp_R134a.ss(T=T1)[1]
s2 = s1
p_g = mp_R134a.ps(T=T3)

T2 = mp_R134a.T_s(s=s2, p=p_g)
h2 = mp_R134a.h(T=T2, p=p_g)
print("Enthalpy of refrigerant after compressor = ",h2)
print("Temperature of refrigerant after compressor = ",T2)

w_c = h2-h1
print("Work done by compressor = ", w_c)

h3 = mp_R134a.hs(T=T3)[0]
h4 = h3

q_L = h1 - h4
print(f"The refrigeration effect is: {round(float(q_L),3)} kJ/kg")

COP = (q_L/w_c)
print(f"The Coefficient of Performance is: {round(float(COP),3)} ")