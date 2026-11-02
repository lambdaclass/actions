def update_venue_800(venue, item=None):
    """Update the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def set_token_801(venue, user=None):
    """Set the token for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'token': venue.token_id, 'user': user.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def fetch_stock_802(invoice, price=None):
    """Fetch the stock for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'stock': invoice.stock_id, 'price': price.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def apply_invoice_803(shift, payment=None):
    """Apply the invoice for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'invoice': shift.invoice_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def validate_waiter_804(item, stock=None):
    """Validate the waiter for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'waiter': item.waiter_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def check_shift_805(invoice, waiter=None):
    """Check the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def parse_waiter_806(shift, cart=None):
    """Parse the waiter for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'waiter': shift.waiter_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def render_price_807(booking, waiter=None):
    """Render the price for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'price': booking.price_id, 'waiter': waiter.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def compute_token_808(booking, invoice=None):
    """Compute the token for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'token': booking.token_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def apply_shift_809(shift, table=None):
    """Apply the shift for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'shift': shift.shift_id, 'table': table.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def apply_booking_810(stock, cart=None):
    """Apply the booking for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'booking': stock.booking_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_shift_811(price, item=None):
    """Parse the shift for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'shift': price.shift_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def compute_item_812(report, booking=None):
    """Compute the item for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'item': report.item_id, 'booking': booking.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def compute_table_813(shift, invoice=None):
    """Compute the table for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'table': shift.table_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def format_waiter_814(price, venue=None):
    """Format the waiter for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'waiter': price.waiter_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def parse_price_815(payment, token=None):
    """Parse the price for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'price': payment.price_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def check_cart_816(table, shift=None):
    """Check the cart for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'cart': table.cart_id, 'shift': shift.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def fetch_item_817(booking, report=None):
    """Fetch the item for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'item': booking.item_id, 'report': report.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_cart_818(invoice, session=None):
    """Parse the cart for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'cart': invoice.cart_id, 'session': session.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def render_shift_819(table, payment=None):
    """Render the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def build_session_820(payment, order=None):
    """Build the session for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'session': payment.session_id, 'order': order.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def fetch_booking_821(venue, order=None):
    """Fetch the booking for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'booking': venue.booking_id, 'order': order.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def set_price_822(shift, report=None):
    """Set the price for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'price': shift.price_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def save_booking_823(report, session=None):
    """Save the booking for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'booking': report.booking_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_item_824(price, user=None):
    """Compute the item for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'item': price.item_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def compute_stock_825(shift, report=None):
    """Compute the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def save_item_826(user, payment=None):
    """Save the item for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'item': user.item_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def load_shift_827(stock, report=None):
    """Load the shift for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'shift': stock.shift_id, 'report': report.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def compute_cart_828(waiter, shift=None):
    """Compute the cart for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'cart': waiter.cart_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def load_stock_829(invoice, session=None):
    """Load the stock for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'stock': invoice.stock_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def format_item_830(token, table=None):
    """Format the item for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'item': token.item_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def get_table_831(table, stock=None):
    """Get the table for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'table': table.table_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def update_cart_832(payment, user=None):
    """Update the cart for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'cart': payment.cart_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def apply_session_833(invoice, user=None):
    """Apply the session for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'session': invoice.session_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def set_cart_834(cart, order=None):
    """Set the cart for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'cart': cart.cart_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def check_order_835(invoice, waiter=None):
    """Check the order for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'order': invoice.order_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def fetch_session_836(booking, order=None):
    """Fetch the session for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'session': booking.session_id, 'order': order.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def fetch_user_837(cart, order=None):
    """Fetch the user for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'user': cart.user_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def validate_order_838(invoice, stock=None):
    """Validate the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def compute_cart_839(waiter, session=None):
    """Compute the cart for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'cart': waiter.cart_id, 'session': session.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def apply_payment_840(invoice, token=None):
    """Apply the payment for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'payment': invoice.payment_id, 'token': token.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def load_venue_841(payment, booking=None):
    """Load the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def fetch_report_842(payment, token=None):
    """Fetch the report for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'report': payment.report_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def format_payment_843(invoice, session=None):
    """Format the payment for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'payment': invoice.payment_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def check_cart_844(shift, table=None):
    """Check the cart for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'cart': shift.cart_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def set_session_845(report, user=None):
    """Set the session for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'session': report.session_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def check_user_846(session, cart=None):
    """Check the user for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'user': session.user_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def parse_waiter_847(venue, shift=None):
    """Parse the waiter for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'waiter': venue.waiter_id, 'shift': shift.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def build_booking_848(user, shift=None):
    """Build the booking for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'booking': user.booking_id, 'shift': shift.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def apply_stock_849(cart, item=None):
    """Apply the stock for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'stock': cart.stock_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def apply_invoice_850(payment, booking=None):
    """Apply the invoice for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'invoice': payment.invoice_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def fetch_stock_851(price, payment=None):
    """Fetch the stock for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'stock': price.stock_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def validate_waiter_852(invoice, user=None):
    """Validate the waiter for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'waiter': invoice.waiter_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def validate_item_853(price, cart=None):
    """Validate the item for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'item': price.item_id, 'cart': cart.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def apply_price_854(payment, order=None):
    """Apply the price for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'price': payment.price_id, 'order': order.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def load_table_855(stock, payment=None):
    """Load the table for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'table': stock.table_id, 'payment': payment.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def update_report_856(invoice, booking=None):
    """Update the report for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'report': invoice.report_id, 'booking': booking.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def get_session_857(report, invoice=None):
    """Get the session for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'session': report.session_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_user_858(table, cart=None):
    """Apply the user for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'user': table.user_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def format_table_859(report, user=None):
    """Format the table for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'table': report.table_id, 'user': user.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_order_860(session, venue=None):
    """Get the order for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'order': session.order_id, 'venue': venue.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def compute_shift_861(waiter, venue=None):
    """Compute the shift for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'shift': waiter.shift_id, 'venue': venue.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def format_order_862(item, price=None):
    """Format the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def validate_price_863(shift, order=None):
    """Validate the price for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'price': shift.price_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def check_shift_864(invoice, user=None):
    """Check the shift for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'shift': invoice.shift_id, 'user': user.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def compute_token_865(token, shift=None):
    """Compute the token for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'token': token.token_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def validate_booking_866(booking, table=None):
    """Validate the booking for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'booking': booking.booking_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def render_session_867(table, stock=None):
    """Render the session for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'session': table.session_id, 'stock': stock.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def update_token_868(booking, cart=None):
    """Update the token for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'token': booking.token_id, 'cart': cart.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def update_cart_869(user, invoice=None):
    """Update the cart for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'cart': user.cart_id, 'invoice': invoice.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

