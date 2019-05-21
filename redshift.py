from __future__ import print_function, division
import numpy as np

while True:

	to_calc = raw_input('What would you like to calculate? (z/d): ')

	if (to_calc == 'd'):
		z = float(raw_input('Value of z: '))

		H = 65
		c = 3 * 10**5
	
		v = z * c

		d = v / H

		print('The distance is', d, 'Mpc.')

	elif (to_calc == 'z'):
		orig = float(raw_input('Original wavelength: '))
		new = float(raw_input('Shifted wavelength: '))
		delta = new - orig
		z = np.abs(delta / orig)
	
		if (delta > 0):
			print('Your object has a redshift of', z)
		else:
			print('Your object has a blueshift of', z)

	tocontinue = raw_input('Would you like to do another? (y/n) ')

	if (tocontinue == 'y'):
		continue
	else:
		break
	
