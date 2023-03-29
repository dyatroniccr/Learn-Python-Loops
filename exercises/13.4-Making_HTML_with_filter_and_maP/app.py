all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(listColors):    
    return list(filter(lambda color: color['sexy'], listColors))


def generate_li(printColors):
	return list(map(lambda x: f"<li>{x['label']}</li>", printColors ))

print(generate_li(filter_colors(all_colors)))
