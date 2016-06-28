def intersection(rect1, rect2):
	if rect1['x_left'] >= rect2['x_right'] or rect1['x_right'] <= rect2['x_left']:
		return {}

	if rect1['y_down'] >= rect2['y_down'] or rect1['y_up'] <= rect2['y_down']:
		return {}

	# This guarantees intersection
	ret = {}

	ret.add('x_left', max(rect1['x_left'], rect2['x_left']))
	ret.add('x_right', min(rect1['x_right'], rect2['x_right']))
	ret.add('y_down', max(rect1['y_down'], rect2['y_down']))
	ret.add('y_up', min(rect1['y_up'], rect2['y_up']))

	return ret

