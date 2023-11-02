import numpy as np

# Use these constants to adjust the size of the training sets
NSAMPLES = 1000 # target number of sample for this example
DRAINAGE_TO_IMBIBITION = 0.015 # probability to switch to imbibition
MAX_SAT_STEP = 0.005       # maximum step in saturation for the next sample

# drainage
Smin_drainage = 0.1
Smax_drainage = 0.9
#N_drainage = 2             # power for the Corey function
kmax_drainage = 1.0        # maximum relative permeability

# imbibition
Smin_imbibition = 0.4      # imbibition results in more trapped gas
#N_drainage = 2             # power for the Corey function



# At the turning point from drainage to imbibition process we
# estimate the residual
def imbibition_residual_saturation(Smin,Smax,Sturn):
    C = (1/Smin)-(1/Smax)
    Snw_residual = Sturn/(1 + C*Sturn)
    return Snw_residual

# relative permeability from Corey
def rel_perm_corey(S,Smax,Smin,krmax=1.0,N=2.0):
    #S = 1-S
    S_N = (S-Smin)/(Smax-Smin)
    kr = krmax*np.power(S_N,N)
    return kr

def summary_plot(x_data,y_data):
    ### basic plot of the results of generating a training set
    import matplotlib.pyplot as plt

    # Create the scatter plot
    plt.scatter(x_data, y_data)

    # Customize the plot if desired
    plt.title('Scatter Plot')
    plt.xlabel('S (saturation of non-wetting phase)')
    plt.ylabel('Kr (relative permeability)')

    # Display the plot
    plt.show()


kmax_drainage = 1.0

S = Smin_drainage  # we start with the non-wetting phase at its minimum saturation
Smin = Smin_drainage
Smax = Smax_drainage
kmax = kmax_drainage

# we drain the wetting phase, then flood it back in, then drain, then flood etc.
# This mean that the saturation of the non-wetting phase increases along a drainage curve and
# decreases along an imbibition curve and over time more and more of the non-wetting phase
# gets trapped.

# pick the number of turning points
bDrainage = True # are we draining or imbibing?

S_store=[]
kr_store=[]
for a in range(NSAMPLES):
    delta_S  = np.random.rand(1)[0]*MAX_SAT_STEP
    if bDrainage:
        S+=delta_S
    else:
        S-=delta_S

    kr = rel_perm_corey(S,Smax,Smin,krmax=kmax)
    S_store.append(S)
    kr_store.append(kr)

    # approximately 5 drainage peaks
    if bDrainage==True and np.random.rand(1)[0]<DRAINAGE_TO_IMBIBITION:
        Smin = imbibition_residual_saturation(Smin_imbibition,Smax,S)
        kmax = kr_store[-1]
        Smax = S
        bDrainage = False

    # turn around when we get to Smin
    if S<Smin:
        bDrainage=True
        Smin = Smin_drainage
        Smax = Smax_drainage
        kmax = kmax_drainage

    # at the end we are on the imbibition curve
    if S>Smax:
        Smin = imbibition_residual_saturation(Smin_imbibition,Smax,S)
        bDrainage = False

summary_plot(S_store,kr_store)
