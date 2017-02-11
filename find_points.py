import sys
import fiona
from shapely.geometry import geo, Point

class PointFinder(object):
  """Finds points in a given shapefile"""
  def __init__(self, shapefile_filename, points_filename):
    self.shapefile_filename = shapefile_filename
    self.points_filename = points_filename
    self._load_points()

  def check_all_points(self):
    format_string = "POINT({}, {})\tIn Shapefile? {}"
    for point in self.points:
      x = point.x
      y = point.y
      contains_point = self.contains_point(point)
      print(format_string.format(x, y, contains_point))

  def contains_point(self, point):
    with fiona.open(self.shapefile_filename) as fiona_collection:
      shapefile_record = fiona_collection.next()
      if 'geometry' in shapefile_record:
        shape = geo.asShape(shapefile_record['geometry'])
        if shape.contains(point):
          return True
    return False


  # This function expects the points file to be a csv with
  # the header: `id,lat,lon`
  def _load_points(self):
    lines = [line[0:-1] for line in open(self.points_filename, 'r')][1:]
    self.points = map(self._load_point, lines)

  def _load_point(self, point_string):
    split_point_string = point_string.split(',')
    return Point(float(split_point_string[2]),
                 float(split_point_string[1]))


def main():
  if len(sys.argv) < 2:
    print("Usage: python find_points.py <shapefile_filename> <points_filename>")
  pf = PointFinder(sys.argv[1], sys.argv[2])
  pf.check_all_points()

if __name__ == '__main__':
  main()
