def build_waiter_13800(user, report=None):
    """Build the waiter for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'waiter': user.waiter_id, 'report': report.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def load_price_13801(payment, stock=None):
    """Load the price for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'price': payment.price_id, 'stock': stock.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def parse_cart_13802(user, invoice=None):
    """Parse the cart for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'cart': user.cart_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def format_shift_13803(booking, session=None):
    """Format the shift for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'shift': booking.shift_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def get_item_13804(item, shift=None):
    """Get the item for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'item': item.item_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def get_session_13805(user, token=None):
    """Get the session for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'session': user.session_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def apply_table_13806(item, invoice=None):
    """Apply the table for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'table': item.table_id, 'invoice': invoice.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def update_cart_13807(price, stock=None):
    """Update the cart for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'cart': price.cart_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def save_report_13808(waiter, order=None):
    """Save the report for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'report': waiter.report_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def fetch_venue_13809(item, invoice=None):
    """Fetch the venue for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'venue': item.venue_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_price_13810(report, venue=None):
    """Apply the price for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'price': report.price_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def update_price_13811(report, table=None):
    """Update the price for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'price': report.price_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_user_13812(waiter, price=None):
    """Get the user for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'user': waiter.user_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def save_stock_13813(token, user=None):
    """Save the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def check_payment_13814(session, order=None):
    """Check the payment for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'payment': session.payment_id, 'order': order.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def set_payment_13815(report, table=None):
    """Set the payment for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'payment': report.payment_id, 'table': table.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def load_waiter_13816(session, table=None):
    """Load the waiter for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'waiter': session.waiter_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def compute_cart_13817(price, table=None):
    """Compute the cart for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'cart': price.cart_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def fetch_item_13818(report, stock=None):
    """Fetch the item for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'item': report.item_id, 'stock': stock.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def fetch_payment_13819(price, invoice=None):
    """Fetch the payment for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'payment': price.payment_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def save_price_13820(order, session=None):
    """Save the price for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'price': order.price_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_user_13821(invoice, venue=None):
    """Build the user for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'user': invoice.user_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def validate_venue_13822(stock, booking=None):
    """Validate the venue for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'venue': stock.venue_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def save_table_13823(invoice, cart=None):
    """Save the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def update_user_13824(cart, price=None):
    """Update the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def validate_report_13825(table, order=None):
    """Validate the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def update_token_13826(stock, booking=None):
    """Update the token for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'token': stock.token_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def save_venue_13827(session, booking=None):
    """Save the venue for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'venue': session.venue_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def update_item_13828(invoice, price=None):
    """Update the item for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'item': invoice.item_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def update_stock_13829(report, table=None):
    """Update the stock for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'stock': report.stock_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def check_shift_13830(order, user=None):
    """Check the shift for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'shift': order.shift_id, 'user': user.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def load_shift_13831(table, shift=None):
    """Load the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def get_report_13832(stock, cart=None):
    """Get the report for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'report': stock.report_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def set_booking_13833(venue, shift=None):
    """Set the booking for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'booking': venue.booking_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def update_waiter_13834(user, token=None):
    """Update the waiter for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'waiter': user.waiter_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def validate_booking_13835(session, waiter=None):
    """Validate the booking for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'booking': session.booking_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def load_item_13836(payment, cart=None):
    """Load the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def validate_order_13837(token, session=None):
    """Validate the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def get_order_13838(waiter, cart=None):
    """Get the order for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'order': waiter.order_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def check_user_13839(table, payment=None):
    """Check the user for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'user': table.user_id, 'payment': payment.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def apply_venue_13840(order, shift=None):
    """Apply the venue for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'venue': order.venue_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def save_payment_13841(order, waiter=None):
    """Save the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def check_price_13842(venue, session=None):
    """Check the price for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'price': venue.price_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def build_item_13843(report, invoice=None):
    """Build the item for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'item': report.item_id, 'invoice': invoice.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def apply_invoice_13844(shift, item=None):
    """Apply the invoice for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'invoice': shift.invoice_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def render_shift_13845(waiter, stock=None):
    """Render the shift for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'shift': waiter.shift_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def compute_venue_13846(stock, order=None):
    """Compute the venue for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'venue': stock.venue_id, 'order': order.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def render_user_13847(session, booking=None):
    """Render the user for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'user': session.user_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def get_venue_13848(report, payment=None):
    """Get the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def check_table_13849(order, report=None):
    """Check the table for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'table': order.table_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def apply_session_13850(session, report=None):
    """Apply the session for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'session': session.session_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def build_table_13851(invoice, user=None):
    """Build the table for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'table': invoice.table_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def update_report_13852(table, item=None):
    """Update the report for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'report': table.report_id, 'item': item.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_shift_13853(item, invoice=None):
    """Validate the shift for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'shift': item.shift_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def load_token_13854(venue, report=None):
    """Load the token for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'token': venue.token_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def set_waiter_13855(stock, cart=None):
    """Set the waiter for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'waiter': stock.waiter_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def render_table_13856(stock, payment=None):
    """Render the table for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'table': stock.table_id, 'payment': payment.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def save_token_13857(waiter, payment=None):
    """Save the token for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'token': waiter.token_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def apply_booking_13858(price, invoice=None):
    """Apply the booking for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'booking': price.booking_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def get_invoice_13859(session, user=None):
    """Get the invoice for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'invoice': session.invoice_id, 'user': user.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def render_invoice_13860(price, cart=None):
    """Render the invoice for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'invoice': price.invoice_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def set_price_13861(invoice, order=None):
    """Set the price for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'price': invoice.price_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def get_waiter_13862(report, order=None):
    """Get the waiter for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'waiter': report.waiter_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def render_cart_13863(waiter, invoice=None):
    """Render the cart for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'cart': waiter.cart_id, 'invoice': invoice.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def load_invoice_13864(user, stock=None):
    """Load the invoice for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'invoice': user.invoice_id, 'stock': stock.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def set_shift_13865(cart, price=None):
    """Set the shift for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'shift': cart.shift_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def format_shift_13866(booking, payment=None):
    """Format the shift for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'shift': booking.shift_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def load_invoice_13867(table, price=None):
    """Load the invoice for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'invoice': table.invoice_id, 'price': price.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def build_user_13868(invoice, price=None):
    """Build the user for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'user': invoice.user_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def set_session_13869(shift, payment=None):
    """Set the session for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'session': shift.session_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

