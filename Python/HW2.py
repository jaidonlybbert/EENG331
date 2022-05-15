import math

unCox= 200E-6 # A/V^2
Vth  = 0.4    # Volts
Vth_pmos = -0.4 # Volts
# Problem 1
Rd   = 500    # Ohms
W_L  = 10/0.18
VGS  = 1 # Volt
Vov  = VGS - Vth

Vds = Vov

Id = 0.5*unCox*W_L*Vov*Vov
Vdd = Id*Rd+Vds

print("Problem 1:\n Vdd =", Vdd, "\n\n")

# Problem 2: find W/L
# Given
gm = 1/50 # mhos
Id = 0.5E-3 # Amps

W_L = (gm*gm)/(2*unCox*Id)

print("Problem 2:\n W_L =", W_L, "\n\n")

# Problem 5: Find W_L
upCox = 100E-6
Id = 0.7E-3
Vov = 0.4

W_L = 2*Id/(upCox*Vov*Vov)
print("Problem 5: \n W_L=", W_L, "\n\n")

# Problem 7: Find Id
# Finding through iteration

Vdd = 1.8
unCox = 100E-6
W = 10
L = 0.18
W_L = W/L
R1 = 5E3
R2 = 12E3
Rs = 500
Rd = 2.25E3
Vth = 0.5

Vg = Vdd*R2/(R1+R2)
Vgs = Vg-0.3
err = 100
print("Problem 7:\n\n")

while (err>0.001):
    old_Id = (Vg-Vgs)/Rs
    Vgs = Vth+math.sqrt(2*old_Id/(unCox*W_L))
    new_Id = (Vg-Vgs)/Rs
    Vgs = Vth+math.sqrt(2*new_Id/(unCox*W_L))
    
    err = (new_Id-old_Id)/old_Id
    print("Id =", new_Id, "\nVgs =", Vgs, "\nErr =", err, "\n\n")


# Problem 8: Find Rd

print("Problem 8:\n\n")

Vth = 0.4
Vdd = 1.8
gm = 1/100
Id = 1E-3

Vgs = 2*Id/gm+Vth
Rd = (Vdd-Vgs)/Id

print("Rd =", Rd, "\n\n")
