from webapp import server as router

from flask import render_template, request

@router.route('/')
def index():
    return render_template('index.html')

@router.route('/trip', methods=['GET'])
def tripfinder():
    from_ = request.args.get('trip-from')
    to_ = request.args.get('trip-to')
    at_ = request.args.get('trip-at')
    if from_ is None or to_ is None or at_ is None:
        from_ = ''
        to_ = ''
        at_ = ''
    
    # get the information from the page load. If it doesn't come, skip this.
    
    if not from_ == '' and not to_ == '' and not at_ == '':
        message = 'The database results go here. We probably want to template a list.'
    else:
        message = 'Can you provide more information?'
    
    return render_template('find_trip.html', from_=from_, to_=to_, at_=at_, message=message)