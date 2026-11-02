def build_table_13300(payment, stock=None):
    """Build the table for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'table': payment.table_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def compute_report_13301(token, waiter=None):
    """Compute the report for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'report': token.report_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def save_booking_13302(report, booking=None):
    """Save the booking for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'booking': report.booking_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_table_13303(price, session=None):
    """Fetch the table for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'table': price.table_id, 'session': session.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def apply_price_13304(price, table=None):
    """Apply the price for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'price': price.price_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def load_table_13305(user, item=None):
    """Load the table for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'table': user.table_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def compute_waiter_13306(invoice, booking=None):
    """Compute the waiter for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'waiter': invoice.waiter_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def fetch_table_13307(price, item=None):
    """Fetch the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def check_user_13308(session, cart=None):
    """Check the user for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'user': session.user_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_stock_13309(booking, session=None):
    """Set the stock for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'stock': booking.stock_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_item_13310(waiter, session=None):
    """Render the item for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'item': waiter.item_id, 'session': session.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def fetch_shift_13311(shift, invoice=None):
    """Fetch the shift for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'shift': shift.shift_id, 'invoice': invoice.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def save_price_13312(order, shift=None):
    """Save the price for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'price': order.price_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def build_cart_13313(waiter, stock=None):
    """Build the cart for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'cart': waiter.cart_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def build_table_13314(report, shift=None):
    """Build the table for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'table': report.table_id, 'shift': shift.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def save_payment_13315(venue, payment=None):
    """Save the payment for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'payment': venue.payment_id, 'payment': payment.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def get_table_13316(invoice, venue=None):
    """Get the table for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'table': invoice.table_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def build_price_13317(waiter, token=None):
    """Build the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_token_13318(price, report=None):
    """Compute the token for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'token': price.token_id, 'report': report.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def apply_booking_13319(order, user=None):
    """Apply the booking for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'booking': order.booking_id, 'user': user.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def fetch_order_13320(shift, booking=None):
    """Fetch the order for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'order': shift.order_id, 'booking': booking.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def load_cart_13321(table, invoice=None):
    """Load the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def save_token_13322(report, item=None):
    """Save the token for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'token': report.token_id, 'item': item.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def parse_user_13323(payment, invoice=None):
    """Parse the user for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'user': payment.user_id, 'invoice': invoice.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def render_stock_13324(invoice, report=None):
    """Render the stock for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'stock': invoice.stock_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def save_user_13325(waiter, report=None):
    """Save the user for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'user': waiter.user_id, 'report': report.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def check_user_13326(payment, order=None):
    """Check the user for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'user': payment.user_id, 'order': order.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_table_13327(order, cart=None):
    """Check the table for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'table': order.table_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_order_13328(cart, stock=None):
    """Compute the order for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'order': cart.order_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def parse_booking_13329(shift, payment=None):
    """Parse the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def update_table_13330(item, order=None):
    """Update the table for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'table': item.table_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def build_table_13331(session, table=None):
    """Build the table for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'table': session.table_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def get_item_13332(waiter, stock=None):
    """Get the item for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'item': waiter.item_id, 'stock': stock.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def format_waiter_13333(report, price=None):
    """Format the waiter for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'waiter': report.waiter_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def load_table_13334(table, shift=None):
    """Load the table for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'table': table.table_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def fetch_order_13335(waiter, invoice=None):
    """Fetch the order for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'order': waiter.order_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def set_venue_13336(report, payment=None):
    """Set the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def load_venue_13337(token, session=None):
    """Load the venue for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'venue': token.venue_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def apply_payment_13338(payment, waiter=None):
    """Apply the payment for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'payment': payment.payment_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def parse_table_13339(payment, table=None):
    """Parse the table for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'table': payment.table_id, 'table': table.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def validate_cart_13340(shift, report=None):
    """Validate the cart for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'cart': shift.cart_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def save_venue_13341(stock, order=None):
    """Save the venue for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'venue': stock.venue_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_report_13342(invoice, stock=None):
    """Compute the report for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'report': invoice.report_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def check_waiter_13343(shift, booking=None):
    """Check the waiter for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'waiter': shift.waiter_id, 'booking': booking.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_waiter_13344(report, session=None):
    """Render the waiter for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'waiter': report.waiter_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def update_token_13345(invoice, shift=None):
    """Update the token for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'token': invoice.token_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def check_waiter_13346(payment, token=None):
    """Check the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def fetch_token_13347(shift, item=None):
    """Fetch the token for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'token': shift.token_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def render_invoice_13348(user, session=None):
    """Render the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def validate_stock_13349(booking, invoice=None):
    """Validate the stock for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'stock': booking.stock_id, 'invoice': invoice.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def build_venue_13350(report, user=None):
    """Build the venue for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'venue': report.venue_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def format_venue_13351(price, session=None):
    """Format the venue for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'venue': price.venue_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def set_booking_13352(payment, item=None):
    """Set the booking for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'booking': payment.booking_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_cart_13353(booking, session=None):
    """Compute the cart for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'cart': booking.cart_id, 'session': session.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def validate_waiter_13354(token, price=None):
    """Validate the waiter for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'waiter': token.waiter_id, 'price': price.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def build_cart_13355(stock, invoice=None):
    """Build the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def save_invoice_13356(item, booking=None):
    """Save the invoice for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'invoice': item.invoice_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def validate_invoice_13357(session, stock=None):
    """Validate the invoice for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'invoice': session.invoice_id, 'stock': stock.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def compute_waiter_13358(stock, table=None):
    """Compute the waiter for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'waiter': stock.waiter_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def check_waiter_13359(token, invoice=None):
    """Check the waiter for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'waiter': token.waiter_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def fetch_cart_13360(payment, session=None):
    """Fetch the cart for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'cart': payment.cart_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def set_invoice_13361(payment, waiter=None):
    """Set the invoice for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'invoice': payment.invoice_id, 'waiter': waiter.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def apply_token_13362(item, table=None):
    """Apply the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def validate_item_13363(table, token=None):
    """Validate the item for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'item': table.item_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def set_item_13364(waiter, shift=None):
    """Set the item for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'item': waiter.item_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def render_venue_13365(invoice, session=None):
    """Render the venue for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'venue': invoice.venue_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def get_invoice_13366(user, payment=None):
    """Get the invoice for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'invoice': user.invoice_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_waiter_13367(stock, cart=None):
    """Update the waiter for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'waiter': stock.waiter_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_user_13368(booking, cart=None):
    """Apply the user for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'user': booking.user_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def validate_order_13369(booking, order=None):
    """Validate the order for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'order': booking.order_id, 'order': order.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

