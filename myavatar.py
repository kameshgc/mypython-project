import py_avataaars as pa
avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.BLACK,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    facial_hair_color=pa.HairColor.BROWN,
    top_type=pa.TopType.LONG_HAIR_BIG_HAIR,
    hat_color=pa.Color.BLACK,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.DEFAULT,
    eyebrow_type=pa.EyebrowType.DEFAULT,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
    clothe_type=pa.ClotheType.SHIRT_SCOOP_NECK,
    clothe_color=pa.Color.HEATHER,
    clothe_graphic_type=pa.ClotheGraphicType.RESIST,
)
avatar.render_png_file('demo.png')