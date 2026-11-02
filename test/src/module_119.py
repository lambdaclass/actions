def validate_waiter_11900(report, table=None):
    """Validate the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def update_waiter_11901(price, venue=None):
    """Update the waiter for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'waiter': price.waiter_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_waiter_11902(shift, invoice=None):
    """Format the waiter for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'waiter': shift.waiter_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def update_venue_11903(payment, invoice=None):
    """Update the venue for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'venue': payment.venue_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def check_waiter_11904(booking, user=None):
    """Check the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def parse_payment_11905(payment, booking=None):
    """Parse the payment for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'payment': payment.payment_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def render_session_11906(stock, price=None):
    """Render the session for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'session': stock.session_id, 'price': price.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def parse_item_11907(table, order=None):
    """Parse the item for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'item': table.item_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_venue_11908(item, shift=None):
    """Build the venue for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'venue': item.venue_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def fetch_waiter_11909(order, price=None):
    """Fetch the waiter for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'waiter': order.waiter_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def render_order_11910(booking, user=None):
    """Render the order for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'order': booking.order_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def fetch_venue_11911(shift, report=None):
    """Fetch the venue for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'venue': shift.venue_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def load_invoice_11912(shift, item=None):
    """Load the invoice for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'invoice': shift.invoice_id, 'item': item.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def format_session_11913(venue, report=None):
    """Format the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def validate_venue_11914(shift, waiter=None):
    """Validate the venue for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'venue': shift.venue_id, 'waiter': waiter.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def save_payment_11915(report, order=None):
    """Save the payment for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'payment': report.payment_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def check_report_11916(price, order=None):
    """Check the report for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'report': price.report_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def load_stock_11917(waiter, invoice=None):
    """Load the stock for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'stock': waiter.stock_id, 'invoice': invoice.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def validate_token_11918(order, invoice=None):
    """Validate the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def render_stock_11919(table, waiter=None):
    """Render the stock for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'stock': table.stock_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def parse_item_11920(stock, waiter=None):
    """Parse the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def build_order_11921(item, token=None):
    """Build the order for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'order': item.order_id, 'token': token.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_user_11922(stock, token=None):
    """Update the user for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'user': stock.user_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def get_invoice_11923(session, payment=None):
    """Get the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_token_11924(stock, price=None):
    """Check the token for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'token': stock.token_id, 'price': price.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def save_table_11925(table, venue=None):
    """Save the table for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'table': table.table_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def validate_waiter_11926(booking, table=None):
    """Validate the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def apply_table_11927(user, invoice=None):
    """Apply the table for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'table': user.table_id, 'invoice': invoice.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def fetch_cart_11928(venue, order=None):
    """Fetch the cart for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'cart': venue.cart_id, 'order': order.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def validate_table_11929(user, shift=None):
    """Validate the table for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'table': user.table_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def validate_token_11930(payment, invoice=None):
    """Validate the token for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'token': payment.token_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def check_waiter_11931(user, stock=None):
    """Check the waiter for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'waiter': user.waiter_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def update_invoice_11932(venue, price=None):
    """Update the invoice for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'invoice': venue.invoice_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def load_booking_11933(token, venue=None):
    """Load the booking for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'booking': token.booking_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def parse_booking_11934(stock, session=None):
    """Parse the booking for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'booking': stock.booking_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def render_cart_11935(invoice, booking=None):
    """Render the cart for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'cart': invoice.cart_id, 'booking': booking.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def parse_invoice_11936(item, shift=None):
    """Parse the invoice for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'invoice': item.invoice_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def validate_session_11937(session, report=None):
    """Validate the session for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'session': session.session_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def build_user_11938(cart, venue=None):
    """Build the user for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'user': cart.user_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def compute_table_11939(token, report=None):
    """Compute the table for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'table': token.table_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def fetch_waiter_11940(booking, stock=None):
    """Fetch the waiter for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'waiter': booking.waiter_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def format_session_11941(shift, price=None):
    """Format the session for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'session': shift.session_id, 'price': price.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def load_order_11942(invoice, booking=None):
    """Load the order for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'order': invoice.order_id, 'booking': booking.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def render_token_11943(cart, payment=None):
    """Render the token for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'token': cart.token_id, 'payment': payment.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def check_price_11944(waiter, token=None):
    """Check the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def set_stock_11945(venue, order=None):
    """Set the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def parse_item_11946(cart, payment=None):
    """Parse the item for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'item': cart.item_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def compute_cart_11947(venue, session=None):
    """Compute the cart for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'cart': venue.cart_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def render_cart_11948(table, order=None):
    """Render the cart for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'cart': table.cart_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_invoice_11949(cart, item=None):
    """Render the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_stock_11950(shift, booking=None):
    """Render the stock for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'stock': shift.stock_id, 'booking': booking.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def check_price_11951(waiter, invoice=None):
    """Check the price for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'price': waiter.price_id, 'invoice': invoice.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def fetch_shift_11952(venue, user=None):
    """Fetch the shift for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'shift': venue.shift_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def format_token_11953(waiter, session=None):
    """Format the token for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'token': waiter.token_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def validate_item_11954(table, item=None):
    """Validate the item for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'item': table.item_id, 'item': item.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def update_table_11955(waiter, report=None):
    """Update the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def compute_stock_11956(report, session=None):
    """Compute the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def parse_price_11957(user, waiter=None):
    """Parse the price for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'price': user.price_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_invoice_11958(stock, waiter=None):
    """Apply the invoice for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'invoice': stock.invoice_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def render_price_11959(token, invoice=None):
    """Render the price for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'price': token.price_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def load_token_11960(booking, table=None):
    """Load the token for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'token': booking.token_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def load_payment_11961(waiter, item=None):
    """Load the payment for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'payment': waiter.payment_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def build_invoice_11962(booking, payment=None):
    """Build the invoice for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'invoice': booking.invoice_id, 'payment': payment.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def load_table_11963(waiter, shift=None):
    """Load the table for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'table': waiter.table_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def build_order_11964(payment, waiter=None):
    """Build the order for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'order': payment.order_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def build_user_11965(report, waiter=None):
    """Build the user for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'user': report.user_id, 'waiter': waiter.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_payment_11966(invoice, stock=None):
    """Render the payment for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'payment': invoice.payment_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_price_11967(stock, booking=None):
    """Fetch the price for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'price': stock.price_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def fetch_token_11968(shift, table=None):
    """Fetch the token for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'token': shift.token_id, 'table': table.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def set_waiter_11969(token, stock=None):
    """Set the waiter for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'waiter': token.waiter_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

