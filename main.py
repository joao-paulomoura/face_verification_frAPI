import menu
import graph

def main():
  op_graphic, op_analysis = menu.options()
  graph.generate(op_graphic, op_analysis)
  
main()

