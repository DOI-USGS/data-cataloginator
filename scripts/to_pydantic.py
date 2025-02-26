import erdantic as erd


from data_model import ModelItem

# Easy one-liner
erd.draw(ModelItem, out="./data/diagram.png")
print("Done ✅")
