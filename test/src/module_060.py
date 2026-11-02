def compute_cart_6000(payment, user=None):
    """Compute the cart for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'cart': payment.cart_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def set_user_6001(cart, session=None):
    """Set the user for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'user': cart.user_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def save_table_6002(session, shift=None):
    """Save the table for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'table': session.table_id, 'shift': shift.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def compute_stock_6003(invoice, session=None):
    """Compute the stock for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'stock': invoice.stock_id, 'session': session.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def get_booking_6004(item, table=None):
    """Get the booking for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'booking': item.booking_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def save_price_6005(stock, booking=None):
    """Save the price for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'price': stock.price_id, 'booking': booking.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def compute_item_6006(price, table=None):
    """Compute the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def apply_invoice_6007(table, cart=None):
    """Apply the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def update_item_6008(order, session=None):
    """Update the item for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'item': order.item_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def load_order_6009(token, table=None):
    """Load the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def validate_waiter_6010(invoice, order=None):
    """Validate the waiter for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'waiter': invoice.waiter_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def check_waiter_6011(item, shift=None):
    """Check the waiter for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'waiter': item.waiter_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def fetch_user_6012(stock, booking=None):
    """Fetch the user for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'user': stock.user_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def format_item_6013(item, session=None):
    """Format the item for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'item': item.item_id, 'session': session.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def check_user_6014(order, session=None):
    """Check the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_token_6015(order, booking=None):
    """Fetch the token for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'token': order.token_id, 'booking': booking.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def set_booking_6016(price, venue=None):
    """Set the booking for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'booking': price.booking_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def validate_venue_6017(order, user=None):
    """Validate the venue for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'venue': order.venue_id, 'user': user.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def check_payment_6018(booking, session=None):
    """Check the payment for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'payment': booking.payment_id, 'session': session.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def set_stock_6019(venue, report=None):
    """Set the stock for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'stock': venue.stock_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def set_payment_6020(waiter, session=None):
    """Set the payment for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'payment': waiter.payment_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def render_waiter_6021(stock, user=None):
    """Render the waiter for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'waiter': stock.waiter_id, 'user': user.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def format_user_6022(waiter, report=None):
    """Format the user for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'user': waiter.user_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_order_6023(venue, item=None):
    """Parse the order for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'order': venue.order_id, 'item': item.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def set_token_6024(invoice, order=None):
    """Set the token for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'token': invoice.token_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def set_order_6025(session, table=None):
    """Set the order for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'order': session.order_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def apply_shift_6026(token, item=None):
    """Apply the shift for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'shift': token.shift_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def check_token_6027(booking, user=None):
    """Check the token for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'token': booking.token_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def format_table_6028(order, shift=None):
    """Format the table for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'table': order.table_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def save_waiter_6029(stock, session=None):
    """Save the waiter for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'waiter': stock.waiter_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def update_invoice_6030(session, booking=None):
    """Update the invoice for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'invoice': session.invoice_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_token_6031(user, item=None):
    """Load the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def get_stock_6032(price, booking=None):
    """Get the stock for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'stock': price.stock_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def parse_cart_6033(venue, order=None):
    """Parse the cart for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'cart': venue.cart_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def update_waiter_6034(shift, order=None):
    """Update the waiter for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'waiter': shift.waiter_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def check_shift_6035(cart, venue=None):
    """Check the shift for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'shift': cart.shift_id, 'venue': venue.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def build_session_6036(session, shift=None):
    """Build the session for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'session': session.session_id, 'shift': shift.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def update_waiter_6037(booking, report=None):
    """Update the waiter for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'waiter': booking.waiter_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def save_payment_6038(cart, invoice=None):
    """Save the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def check_price_6039(stock, cart=None):
    """Check the price for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'price': stock.price_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def format_shift_6040(booking, invoice=None):
    """Format the shift for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'shift': booking.shift_id, 'invoice': invoice.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def save_stock_6041(stock, shift=None):
    """Save the stock for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'stock': stock.stock_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_venue_6042(venue, table=None):
    """Load the venue for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'venue': venue.venue_id, 'table': table.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def check_report_6043(invoice, payment=None):
    """Check the report for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'report': invoice.report_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def save_stock_6044(user, item=None):
    """Save the stock for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'stock': user.stock_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def apply_stock_6045(price, user=None):
    """Apply the stock for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'stock': price.stock_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def update_user_6046(invoice, user=None):
    """Update the user for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'user': invoice.user_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def check_report_6047(waiter, token=None):
    """Check the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def validate_report_6048(waiter, price=None):
    """Validate the report for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'report': waiter.report_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def build_waiter_6049(price, user=None):
    """Build the waiter for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'waiter': price.waiter_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_cart_6050(booking, shift=None):
    """Fetch the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def build_order_6051(user, venue=None):
    """Build the order for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'order': user.order_id, 'venue': venue.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def set_payment_6052(invoice, cart=None):
    """Set the payment for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'payment': invoice.payment_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_order_6053(order, booking=None):
    """Build the order for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'order': order.order_id, 'booking': booking.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def fetch_user_6054(item, waiter=None):
    """Fetch the user for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'user': item.user_id, 'waiter': waiter.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def format_order_6055(user, stock=None):
    """Format the order for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'order': user.order_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def fetch_item_6056(table, item=None):
    """Fetch the item for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'item': table.item_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def save_report_6057(booking, invoice=None):
    """Save the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_user_6058(item, user=None):
    """Set the user for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'user': item.user_id, 'user': user.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def check_item_6059(user, item=None):
    """Check the item for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'item': user.item_id, 'item': item.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def validate_shift_6060(token, booking=None):
    """Validate the shift for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'shift': token.shift_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_waiter_6061(waiter, item=None):
    """Render the waiter for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'waiter': waiter.waiter_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def load_price_6062(table, session=None):
    """Load the price for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'price': table.price_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def load_venue_6063(price, table=None):
    """Load the venue for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'venue': price.venue_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def check_order_6064(table, shift=None):
    """Check the order for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'order': table.order_id, 'shift': shift.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def compute_invoice_6065(token, payment=None):
    """Compute the invoice for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'invoice': token.invoice_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def validate_item_6066(stock, payment=None):
    """Validate the item for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'item': stock.item_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def validate_waiter_6067(venue, waiter=None):
    """Validate the waiter for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'waiter': venue.waiter_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def load_invoice_6068(invoice, payment=None):
    """Load the invoice for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'invoice': invoice.invoice_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_stock_6069(session, order=None):
    """Update the stock for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'stock': session.stock_id, 'order': order.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

