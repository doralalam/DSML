def newtons_laws(a):
    """
    This function prints Newton's three laws of motion.
    """
    if a==1:
        return f"Newton's First Law: An object at rest stays at rest, and an object in motion stays in motion unless acted upon by a net external force."
    elif a==2:
        return f"Newton's Second Law: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass."
    elif a==3:
        return f"Newton's Third Law: For every action, there is an equal and opposite reaction."
    else:
        return "Invalid"