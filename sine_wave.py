import matplotlib.pyplot as plt
import numpy as np

def generate_sine_wave():
    # Generate x values from 0 to 4π
    x = np.linspace(0, 4*np.pi, 1000)
    
    # Generate y values as sine of x
    y = np.sin(x)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue')
    plt.title('Sine Wave', fontsize=16)
    plt.xlabel('x (radians)', fontsize=12)
    plt.ylabel('sin(x)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Save the plot as an image
    plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    generate_sine_wave()