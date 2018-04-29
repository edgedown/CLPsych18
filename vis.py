import os
import ujson as json

DOC_TEMPLATE = '''<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <title>{id}</title>
    </head>
    <body>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <a class="navbar-brand" href="../index.html">CLPsych18</a>
        <em>#{id}</em>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                  <a class="nav-link" href="{last_id}.html">previous<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item active">
                  <a class="nav-link" href="{next_id}.html">next<span class="sr-only">(current)</span></a>
                </li>
            </ul>
        </div>
        </nav>
    </div>
    <div class="container">
    <table class="table table-sm">
      <thead>
        <tr>
          <th scope="col">gender</th>
          <th scope="col">social_class@11</th>
          <th scope="col">total@11</th>
          <th scope="col">anxiety@11</th>
          <th scope="col">depression@11</th>
          <th scope="col">distress@23</th>
          <th scope="col">distress@33</th>
          <th scope="col">distress@42</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{cntrl_gender}</td>
          <td>{cntrl_a11_social_class}</td>
          <td>{a11_bsag_total}</td>
          <td>{a11_bsag_anxiety}</td>
          <td>{a11_bsag_depression}</td>
          <td>{a23_pdistress}</td>
          <td>{a33_pdistress}</td>
          <td>{a42_pdistress}</td>
        </tr>
      </tbody>
     </table>
    </div>
    <div class="container">
        <h5>Essay</h5>
        {essay}
    </div>
    <div class="container">
        <h5>Corrected essay</h5>
        {corrected_essay}
    </div>
    <div class="container">
        <h5>Features</h5>
        <pre>
        {features}
        </pre>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>'''


TEMPLATE = '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.css">
  
    <title>CLPsych18</title>
  </head>
  <body>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <a class="navbar-brand" href="#">CLPsych18</a>
            <em>Training data</em>
        </nav>
    </div>
    <div class="container">
    <table id="records" class="table table-sm">
      <thead>
        <tr>
          <th scope="col">id</th>
          <th scope="col">gender</th>
          <th scope="col">social_class@11</th>
          <th scope="col">total@11</th>
          <th scope="col">anxiety@11</th>
          <th scope="col">depression@11</th>
          <th scope="col">distress@23</th>
          <th scope="col">distress@33</th>
          <th scope="col">distress@42</th>
        </tr>
      </thead>
      <tbody>
          {}
      </tbody>
     </table>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
    <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.js"></script>
    <script>
'''

ROW = '''
        <tr>
          <td><a href="docs/{id}.html">{id}</a></td>
          <td>{cntrl_gender}</td>
          <td>{cntrl_a11_social_class}</td>
          <td>{a11_bsag_total}</td>
          <td>{a11_bsag_anxiety}</td>
          <td>{a11_bsag_depression}</td>
          <td>{a23_pdistress}</td>
          <td>{a33_pdistress}</td>
          <td>{a42_pdistress}</td>
        </tr>
'''

SCRIPT = '''
$(document).ready(function() {$("table").DataTable();});
'''

POST = '''
    </script>
  </body>
</html>'''


IGNORE = {
    'a11_bsag_total',
    'a11_bsag_anxiety',
    'a11_bsag_depression',
    'a23_pdistress',
    'a33_pdistress',
    'a42_pdistress',
    'essay',
    'id',
}


def write(data, docs, corrected_docs, dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        os.makedirs(os.path.join(dirname, 'docs'))
    ids = list(sorted(data.keys()))
    last_id = '#'
    for i, doc_id in enumerate(ids):
        next_id = ids[i+1] if i < len(ids) - 1 else '#'
        with open(os.path.join(dirname, 'docs', f'{doc_id}.html'), 'w') as f:
            doc_data = data[doc_id]
            doc = docs[doc_id]
            corrected_doc = corrected_docs[doc_id]
            params = {}
            params.update(doc_data)
            features = {}
            for k, v in doc_data.items():
                if k in IGNORE:
                    continue
                features[k] = v
            params['features'] = json.dumps(features, sort_keys=True, indent=2)
            params['essay'] = str(doc)
            params['corrected_essay'] = str(corrected_doc)
            f.write(DOC_TEMPLATE.format(last_id=last_id, next_id=next_id, **params))
        last_id = doc_id

    with open(os.path.join(dirname, 'index.html'), 'w') as f:
        s = TEMPLATE.format('\n'.join(ROW.format(**data[id])
                                          for id in ids))
        s += SCRIPT + POST
        f.write(s)
