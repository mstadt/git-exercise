"""
A simple example for a git workflow
"""

# imports
import matplotlib.pyplot as plt


# define the rhs of system of odes

def main():

    # define the rates dictionary
    rates_dict = {}
    rates_dict["rho"] = 5.
    rates_dict["k"] = 10.

    # define the parameter dictionary (pick whatever values you like!)
    params_dict = {}
    params_dict["U_crit"] = 5.
    params_dict["H"] = 3.
    params_dict["I"] = 6.

    # Solve the system
    def CART_system(y, t):
        C_E, C_P = y
        dydt = [rates_dict["rho"]*C_E, rates_dict["k"]*C_P]
        return dydt

    # plot the system and save the figure
    y0 = [0.1, 0.0]
    
    t = np.linspace(0, 10, 101)
    
    sol = CART_system(pend, y0, t)

    plt.plot(t, sol[:, 0], 'b', label='theta(t)')
    plt.plot(t, sol[:, 1], 'g', label='omega(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

    return 0


if __name__ == '__main__':
    main()
