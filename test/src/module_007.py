def apply_stock_700(shift, venue=None):
    """Apply the stock for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'stock': shift.stock_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def validate_shift_701(item, waiter=None):
    """Validate the shift for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'shift': item.shift_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_token_702(shift, item=None):
    """Render the token for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'token': shift.token_id, 'item': item.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def save_payment_703(venue, waiter=None):
    """Save the payment for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'payment': venue.payment_id, 'waiter': waiter.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def get_order_704(token, booking=None):
    """Get the order for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'order': token.order_id, 'booking': booking.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def set_payment_705(venue, order=None):
    """Set the payment for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'payment': venue.payment_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def get_shift_706(report, order=None):
    """Get the shift for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'shift': report.shift_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def compute_invoice_707(session, invoice=None):
    """Compute the invoice for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'invoice': session.invoice_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def validate_cart_708(stock, user=None):
    """Validate the cart for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'cart': stock.cart_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def render_token_709(user, item=None):
    """Render the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def get_booking_710(price, session=None):
    """Get the booking for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'booking': price.booking_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def update_report_711(payment, order=None):
    """Update the report for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'report': payment.report_id, 'order': order.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def fetch_shift_712(invoice, waiter=None):
    """Fetch the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def fetch_shift_713(token, waiter=None):
    """Fetch the shift for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'shift': token.shift_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def render_venue_714(price, waiter=None):
    """Render the venue for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'venue': price.venue_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def load_venue_715(venue, session=None):
    """Load the venue for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'venue': venue.venue_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def apply_user_716(stock, venue=None):
    """Apply the user for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'user': stock.user_id, 'venue': venue.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def check_waiter_717(report, waiter=None):
    """Check the waiter for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'waiter': report.waiter_id, 'waiter': waiter.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def format_venue_718(report, invoice=None):
    """Format the venue for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'venue': report.venue_id, 'invoice': invoice.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def parse_booking_719(venue, user=None):
    """Parse the booking for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'booking': venue.booking_id, 'user': user.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def update_report_720(table, cart=None):
    """Update the report for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'report': table.report_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def apply_item_721(user, session=None):
    """Apply the item for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'item': user.item_id, 'session': session.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def apply_session_722(payment, table=None):
    """Apply the session for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'session': payment.session_id, 'table': table.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def fetch_price_723(stock, order=None):
    """Fetch the price for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'price': stock.price_id, 'order': order.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def build_price_724(cart, token=None):
    """Build the price for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'price': cart.price_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def apply_venue_725(order, payment=None):
    """Apply the venue for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'venue': order.venue_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def validate_venue_726(booking, order=None):
    """Validate the venue for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'venue': booking.venue_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def get_cart_727(report, user=None):
    """Get the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def parse_table_728(session, table=None):
    """Parse the table for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'table': session.table_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def compute_venue_729(booking, venue=None):
    """Compute the venue for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'venue': booking.venue_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def format_item_730(user, venue=None):
    """Format the item for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'item': user.item_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def check_order_731(invoice, report=None):
    """Check the order for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'order': invoice.order_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def check_user_732(cart, report=None):
    """Check the user for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'user': cart.user_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def validate_cart_733(item, session=None):
    """Validate the cart for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'cart': item.cart_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def check_cart_734(waiter, venue=None):
    """Check the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def set_payment_735(token, waiter=None):
    """Set the payment for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'payment': token.payment_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def update_cart_736(booking, waiter=None):
    """Update the cart for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'cart': booking.cart_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def load_cart_737(venue, stock=None):
    """Load the cart for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'cart': venue.cart_id, 'stock': stock.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def apply_invoice_738(payment, venue=None):
    """Apply the invoice for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'invoice': payment.invoice_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def render_table_739(stock, session=None):
    """Render the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_venue_740(item, price=None):
    """Set the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def apply_waiter_741(invoice, user=None):
    """Apply the waiter for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'waiter': invoice.waiter_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def compute_report_742(shift, table=None):
    """Compute the report for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'report': shift.report_id, 'table': table.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def update_order_743(invoice, token=None):
    """Update the order for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'order': invoice.order_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def compute_shift_744(invoice, user=None):
    """Compute the shift for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'shift': invoice.shift_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def format_user_745(price, payment=None):
    """Format the user for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'user': price.user_id, 'payment': payment.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def build_payment_746(venue, report=None):
    """Build the payment for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'payment': venue.payment_id, 'report': report.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def format_session_747(token, cart=None):
    """Format the session for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'session': token.session_id, 'cart': cart.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def format_user_748(waiter, booking=None):
    """Format the user for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'user': waiter.user_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def load_venue_749(booking, table=None):
    """Load the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def check_report_750(stock, table=None):
    """Check the report for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'report': stock.report_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def update_stock_751(token, venue=None):
    """Update the stock for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'stock': token.stock_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def fetch_token_752(order, item=None):
    """Fetch the token for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'token': order.token_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def load_report_753(price, stock=None):
    """Load the report for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'report': price.report_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def apply_user_754(booking, token=None):
    """Apply the user for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'user': booking.user_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def apply_cart_755(waiter, shift=None):
    """Apply the cart for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'cart': waiter.cart_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def save_report_756(booking, venue=None):
    """Save the report for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'report': booking.report_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def save_waiter_757(booking, table=None):
    """Save the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def save_cart_758(order, item=None):
    """Save the cart for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'cart': order.cart_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def update_order_759(user, booking=None):
    """Update the order for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'order': user.order_id, 'booking': booking.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def update_invoice_760(waiter, report=None):
    """Update the invoice for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'invoice': waiter.invoice_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def apply_booking_761(price, report=None):
    """Apply the booking for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'booking': price.booking_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def apply_price_762(stock, price=None):
    """Apply the price for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'price': stock.price_id, 'price': price.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def fetch_waiter_763(waiter, shift=None):
    """Fetch the waiter for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'waiter': waiter.waiter_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def check_item_764(shift, order=None):
    """Check the item for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'item': shift.item_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def update_session_765(item, cart=None):
    """Update the session for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'session': item.session_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def update_invoice_766(payment, price=None):
    """Update the invoice for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'invoice': payment.invoice_id, 'price': price.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def load_report_767(table, report=None):
    """Load the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def build_report_768(order, token=None):
    """Build the report for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'report': order.report_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def parse_report_769(payment, price=None):
    """Parse the report for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'report': payment.report_id, 'price': price.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

