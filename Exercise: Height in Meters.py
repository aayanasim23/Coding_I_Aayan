def height_in_meters(feet, inches):
    ft_meters = feet * 12 * .0254
    ft_inches = inches * .0254
    return ft_meters + ft_inches

height_in_meters(5,11)