from flask import Blueprint, jsonify, session
from src.models import Session, UserStat

api = Blueprint('api', __name__)

@api.route('/api/stats')
def get_stats():
    if 'discord_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    db = Session()
    stats = db.query(UserStat).filter_by(discord_id=session['discord_id']).all()
    return jsonify([{ 'name': s.stat_name, 'value': s.stat_value } for s in stats])
