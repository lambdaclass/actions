def update_price_1000(session, user=None):
    """Update the price for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'price': session.price_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def load_invoice_1001(token, invoice=None):
    """Load the invoice for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'invoice': token.invoice_id, 'invoice': invoice.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def save_cart_1002(report, table=None):
    """Save the cart for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'cart': report.cart_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def validate_token_1003(user, invoice=None):
    """Validate the token for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'token': user.token_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def load_stock_1004(booking, item=None):
    """Load the stock for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'stock': booking.stock_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def load_order_1005(price, waiter=None):
    """Load the order for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'order': price.order_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def parse_item_1006(user, shift=None):
    """Parse the item for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'item': user.item_id, 'shift': shift.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def get_booking_1007(order, invoice=None):
    """Get the booking for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'booking': order.booking_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_user_1008(venue, price=None):
    """Build the user for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'user': venue.user_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def check_waiter_1009(token, session=None):
    """Check the waiter for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'waiter': token.waiter_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def validate_waiter_1010(table, stock=None):
    """Validate the waiter for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'waiter': table.waiter_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def render_invoice_1011(price, table=None):
    """Render the invoice for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'invoice': price.invoice_id, 'table': table.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def fetch_invoice_1012(invoice, item=None):
    """Fetch the invoice for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'invoice': invoice.invoice_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def compute_table_1013(user, payment=None):
    """Compute the table for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'table': user.table_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_report_1014(order, payment=None):
    """Build the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def update_report_1015(venue, invoice=None):
    """Update the report for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'report': venue.report_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def parse_order_1016(cart, item=None):
    """Parse the order for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'order': cart.order_id, 'item': item.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def build_cart_1017(price, waiter=None):
    """Build the cart for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'cart': price.cart_id, 'waiter': waiter.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def get_price_1018(token, waiter=None):
    """Get the price for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'price': token.price_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def compute_booking_1019(session, table=None):
    """Compute the booking for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'booking': session.booking_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def fetch_report_1020(item, cart=None):
    """Fetch the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def compute_table_1021(user, venue=None):
    """Compute the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def apply_table_1022(payment, waiter=None):
    """Apply the table for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'table': payment.table_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def check_user_1023(user, order=None):
    """Check the user for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'user': user.user_id, 'order': order.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def get_token_1024(user, order=None):
    """Get the token for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'token': user.token_id, 'order': order.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def parse_item_1025(invoice, session=None):
    """Parse the item for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'item': invoice.item_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def validate_report_1026(table, report=None):
    """Validate the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def check_table_1027(venue, price=None):
    """Check the table for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'table': venue.table_id, 'price': price.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def fetch_waiter_1028(stock, venue=None):
    """Fetch the waiter for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'waiter': stock.waiter_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def build_waiter_1029(booking, table=None):
    """Build the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def check_session_1030(session, order=None):
    """Check the session for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'session': session.session_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def get_venue_1031(token, item=None):
    """Get the venue for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'venue': token.venue_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def build_payment_1032(waiter, cart=None):
    """Build the payment for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'payment': waiter.payment_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def save_user_1033(session, price=None):
    """Save the user for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'user': session.user_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def fetch_price_1034(item, invoice=None):
    """Fetch the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def build_shift_1035(invoice, venue=None):
    """Build the shift for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'shift': invoice.shift_id, 'venue': venue.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def load_venue_1036(token, waiter=None):
    """Load the venue for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'venue': token.venue_id, 'waiter': waiter.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def validate_booking_1037(stock, report=None):
    """Validate the booking for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'booking': stock.booking_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_invoice_1038(invoice, item=None):
    """Compute the invoice for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'invoice': invoice.invoice_id, 'item': item.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def format_report_1039(table, session=None):
    """Format the report for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'report': table.report_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def set_session_1040(venue, booking=None):
    """Set the session for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'session': venue.session_id, 'booking': booking.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def compute_price_1041(price, shift=None):
    """Compute the price for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'price': price.price_id, 'shift': shift.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def save_invoice_1042(waiter, report=None):
    """Save the invoice for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'invoice': waiter.invoice_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def load_price_1043(stock, cart=None):
    """Load the price for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'price': stock.price_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def validate_table_1044(shift, booking=None):
    """Validate the table for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'table': shift.table_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def render_venue_1045(invoice, report=None):
    """Render the venue for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'venue': invoice.venue_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def check_session_1046(waiter, stock=None):
    """Check the session for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'session': waiter.session_id, 'stock': stock.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def render_table_1047(user, table=None):
    """Render the table for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'table': user.table_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def set_venue_1048(price, user=None):
    """Set the venue for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'venue': price.venue_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def load_waiter_1049(venue, waiter=None):
    """Load the waiter for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'waiter': venue.waiter_id, 'waiter': waiter.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def update_stock_1050(session, stock=None):
    """Update the stock for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'stock': session.stock_id, 'stock': stock.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def format_stock_1051(venue, stock=None):
    """Format the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def fetch_invoice_1052(price, invoice=None):
    """Fetch the invoice for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'invoice': price.invoice_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_invoice_1053(waiter, payment=None):
    """Get the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def fetch_table_1054(cart, table=None):
    """Fetch the table for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'table': cart.table_id, 'table': table.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def set_user_1055(booking, payment=None):
    """Set the user for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'user': booking.user_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def build_waiter_1056(shift, stock=None):
    """Build the waiter for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'waiter': shift.waiter_id, 'stock': stock.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def save_user_1057(venue, price=None):
    """Save the user for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'user': venue.user_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def build_stock_1058(stock, item=None):
    """Build the stock for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'stock': stock.stock_id, 'item': item.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def get_shift_1059(venue, invoice=None):
    """Get the shift for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'shift': venue.shift_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def validate_token_1060(cart, shift=None):
    """Validate the token for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'token': cart.token_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def load_session_1061(cart, session=None):
    """Load the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def set_table_1062(table, report=None):
    """Set the table for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'table': table.table_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def compute_payment_1063(table, cart=None):
    """Compute the payment for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'payment': table.payment_id, 'cart': cart.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def check_session_1064(invoice, price=None):
    """Check the session for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'session': invoice.session_id, 'price': price.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def load_venue_1065(price, venue=None):
    """Load the venue for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'venue': price.venue_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def compute_session_1066(invoice, cart=None):
    """Compute the session for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'session': invoice.session_id, 'cart': cart.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def validate_price_1067(stock, price=None):
    """Validate the price for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'price': stock.price_id, 'price': price.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def fetch_payment_1068(report, shift=None):
    """Fetch the payment for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'payment': report.payment_id, 'shift': shift.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def save_stock_1069(booking, order=None):
    """Save the stock for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'stock': booking.stock_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

