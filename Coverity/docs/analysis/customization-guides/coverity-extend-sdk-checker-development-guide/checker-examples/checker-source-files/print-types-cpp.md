---
title: "print_types.cpp"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/print_types.cpp.html"
content_id: "Zm8~NimOyuoiPyz666oTzQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:09.237883+00:00"
---

# print_types.cpp

```
// print type information for every local variable
#include "extend-lang.hpp"   // Extend API
#include <string>            // std::string
#include <set>               // std::set
using namespace types;
using namespace std;
// set of classes whose info has been printed
set<string> printedClasses;
// type_recurisve_visitor_t is defined in extend-types.hpp
class ClassTypePrinter : public type_recursive_visitor_t {
public:
  virtual void on_class(const class_type_t &ct);
};
void ClassTypePrinter::on_class(const class_type_t &c)
{
  defined_class_type_t ct = c.load_definition();
  if (!ct) {
    return;
  }
  // obtain qualified name as a string, e.g., "A::B::C"
  ostringstream os;
  os << ct;
  string name = os.str();
  // check to see if we've already printed it
  if (printedClasses.find(name) != printedClasses.end()) {
    return;
  }
  printedClasses.insert(name);
  // print class/struct name
  cout << name << endl;
  // print what this class inherits from
  foreach(p, ct->get_parents()) {
    cout << "  parent: " << p->get_class() << endl;
  }
  // print fields
  foreach(f, ct->get_fields()) {
    cout << "  field: " << (*f)->get_pretty_name()
         << ", type: " << (*f)->get_type() << endl;
  }
  // re-examine field types, looking for classes to print; do this
  // after the above loop so we don't get fields from different
  // classes mixed together
  foreach(f, ct->get_fields()) {
    (*f)->get_type()->visit(*this);
  }
  // similarly for parent classes
  foreach(p, ct->get_parents()) {
    p->get_class()->visit(*this);
  }
}
void printVarInfo(const Expression* varTree)
{
  if (!varTree) {
    return;
  }
  type_t const *t = get_type_of_tree(varTree);
  if (!t) {
    return;
  }
  cout << "local variable:\n"
       << "  file: " << current_file_get_name() << "\n"
       << "  line: " << current_file_lineno() << "\n"
       << "  function: " << current_function_get_name() << "\n"
       << "  var: " << varTree << "\n"
       << "  type: " << *t << endl;
  // visit all the types in 't', looking for classes to print
  ClassTypePrinter ctp;
  ctp(t);
}
START_EXTEND_CHECKER( print_types, simple );
ANALYZE_TREE()
{
  Decl decl;
  if (MATCH(decl)) {
    printVarInfo(decl.var());
  }
}
END_EXTEND_CHECKER();
MAKE_MAIN( print_types )
```
